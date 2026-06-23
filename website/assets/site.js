function html(strings, ...values) {
  return strings.reduce((acc, part, index) => acc + part + (values[index] ?? ""), "");
}

function slugTitle(slug) {
  return slug.replace(/-/g, " ").replace(/\b\w/g, (char) => char.toUpperCase());
}

function rootPath() {
  const root = document.body.dataset.root || "";
  return root ? `${root.replace(/\/$/, "")}/` : "";
}

function siteLink(href) {
  if (!href || /^(https?:|mailto:|#)/.test(href)) return href;
  return `${rootPath()}${href}`;
}

function functionDoc(moduleSlug, name) {
  return window.DATAVIZ_FUNCTION_DOCS?.[moduleSlug]?.[name] || null;
}

function functionHref(moduleSlug, name) {
  const docs = window.DATAVIZ_FUNCTION_DOCS?.[moduleSlug] || {};
  return docs[name]?.href || docs[`${name}_static`]?.href || docs[`${name}_interactive`]?.href || "";
}

function functionCodeLink(moduleSlug, name) {
  const href = functionHref(moduleSlug, name);
  if (!href) return `<code>${name}</code>`;
  return `<a class="code-link" href="${siteLink(href)}"><code>${name}</code></a>`;
}

function submoduleTree(moduleSlug) {
  const docs = window.DATAVIZ_FUNCTION_DOCS?.[moduleSlug] || {};
  const groups = {};
  Object.values(docs).forEach((doc) => {
    const sub = doc.submodule || "_";
    (groups[sub] ||= []).push(doc);
  });
  Object.values(groups).forEach((list) => list.sort((a, b) => a.name.localeCompare(b.name)));
  return Object.keys(groups).sort().map((sub) => ({ name: sub, docs: groups[sub] }));
}

function renderNav() {
  const completed = Object.values(window.DATAVIZ_MODULES).filter((item) => item.status === "complete");
  const planned = Object.values(window.DATAVIZ_MODULES).filter((item) => item.status !== "complete");
  const current = document.body.dataset.page || "";
  const currentModule = document.body.dataset.functionModule || "";
  const currentFunction = document.body.dataset.functionName || "";
  const nav = document.querySelector("[data-nav]");
  if (!nav) return;

  const functionNode = (moduleSlug, doc) => {
    const active = currentModule === moduleSlug && currentFunction === doc.name;
    return html`<li><a class="leaf ${active ? "active" : ""}" href="${siteLink(doc.href)}">${doc.name}</a></li>`;
  };

  const submoduleNode = (moduleSlug, sub, activeSub) => html`
    <li class="nav-sub">
      <details ${activeSub === sub.name ? "open" : ""}>
        <summary>${sub.name}</summary>
        <ul class="nav-list nav-sublist">${sub.docs.map((doc) => functionNode(moduleSlug, doc)).join("")}</ul>
      </details>
    </li>`;

  const moduleNode = (entry) => {
    const isActive = current === entry.slug || currentModule === entry.slug;
    const subs = entry.status === "complete" ? submoduleTree(entry.slug) : [];
    const activeSub = currentModule === entry.slug
      ? (window.DATAVIZ_FUNCTION_DOCS?.[entry.slug]?.[currentFunction]?.submodule || "")
      : "";
    const header = html`
      <summary class="nav-module-summary ${isActive ? "active" : ""}">
        <a class="nav-module-link" href="${siteLink(entry.href)}">
          <span>${entry.title}</span>
          <span class="badge ${entry.status === "complete" ? "" : "todo"}">${entry.status === "complete" ? "Ready" : "Blank"}</span>
        </a>
      </summary>`;
    if (!subs.length) {
      return html`<li class="nav-module"><details ${isActive ? "open" : ""}>${header}</details></li>`;
    }
    return html`
      <li class="nav-module">
        <details ${isActive ? "open" : ""}>
          ${header}
          <ul class="nav-list nav-sublist">${subs.map((sub) => submoduleNode(entry.slug, sub, activeSub)).join("")}</ul>
        </details>
      </li>`;
  };

  nav.innerHTML = html`
    <div class="nav-section">Documentation</div>
    <ul class="nav-list">
      <li><a class="${current === "home" ? "active" : ""}" href="${siteLink("index.html")}">Home</a></li>
      <li><a class="${current === "user-guide" ? "active" : ""}" href="${siteLink("user-guide.html")}">User Guide</a></li>
      <li><a class="${current === "api" ? "active" : ""}" href="${siteLink("api.html")}">API Index</a></li>
      <li><a class="${current === "examples" ? "active" : ""}" href="${siteLink("examples.html")}">Examples</a></li>
      <li><a class="${current === "installation" ? "active" : ""}" href="${siteLink("installation.html")}">Installation</a></li>
      <li><a class="${current === "changelog" ? "active" : ""}" href="${siteLink("changelog.html")}">Changelog</a></li>
    </ul>
    <div class="nav-section">Completed Modules</div>
    <ul class="nav-list nav-tree">${completed.map(moduleNode).join("")}</ul>
    <div class="nav-section">Planned Modules</div>
    <ul class="nav-list nav-tree">${planned.map(moduleNode).join("")}</ul>`;
}

function renderModulePage() {
  const target = document.querySelector("[data-module-page]");
  if (!target) return;
  const slug = target.dataset.modulePage;
  const entry = window.DATAVIZ_MODULES[slug];
  if (!entry) {
    target.innerHTML = `<div class="placeholder"><h1>${slugTitle(slug)}</h1><p>This page is reserved for future documentation.</p></div>`;
    return;
  }
  if (entry.status !== "complete") {
    target.innerHTML = html`
      <section class="hero">
        <p class="eyebrow">Planned module</p>
        <h1>${entry.title}</h1>
        <p class="lead">${entry.summary}</p>
      </section>
      <section class="placeholder">
        <h2>Blank Page</h2>
        <p>This module has not been developed yet. This page is intentionally blank and ready to be updated when implementation begins.</p>
      </section>`;
    return;
  }
  const functions = entry.functions || [];
  target.innerHTML = html`
    <section class="hero">
      <p class="eyebrow">Completed module</p>
      <h1>${entry.title}</h1>
      <p class="lead">${entry.summary}</p>
    </section>
    <div class="stat-row">
      <div class="stat"><strong>${functions.length}</strong><span>public exports</span></div>
      <div class="stat"><strong>${entry.staticCount}</strong><span>static chart APIs</span></div>
      <div class="stat"><strong>${entry.interactiveCount}</strong><span>interactive chart APIs</span></div>
      <div class="stat"><strong>${entry.helperCount}</strong><span>helpers and result types</span></div>
    </div>
    <h2>What This Module Covers</h2>
    <div class="grid">${entry.capabilities.map((cap) => `<div class="card"><h3>${cap.title}</h3><p>${cap.text}</p></div>`).join("")}</div>
    <h2>Common Workflow</h2>
    <pre><code>${entry.example}</code></pre>
    <h2>API Groups</h2>
    <table class="api-table">
      <thead><tr><th>Group</th><th>Functions</th><th>Use when</th></tr></thead>
      <tbody>${entry.groups.map((group) => `<tr><td><strong>${group.name}</strong></td><td>${group.items.map((name) => functionCodeLink(entry.slug, name)).join(" ")}</td><td>${group.use}</td></tr>`).join("")}</tbody>
    </table>
    <h2>Public Exports</h2>
    <ul class="function-list">${functions.map((name) => `<li>${functionCodeLink(entry.slug, name)}</li>`).join("")}</ul>
    <h2>Design Notes</h2>
    <p>${entry.notes}</p>`;
}

function renderApiIndex() {
  const target = document.querySelector("[data-api-index]");
  if (!target) return;
  const completed = Object.values(window.DATAVIZ_MODULES).filter((item) => item.status === "complete");
  target.innerHTML = completed.map((entry) => html`
    <tr>
      <td><a href="${siteLink(entry.href)}">${entry.title}</a></td>
      <td>${entry.summary}</td>
      <td>${entry.functions.length}</td>
    </tr>`).join("");
}

function renderFunctionPage() {
  const target = document.querySelector("[data-function-page]");
  if (!target) return;
  const moduleSlug = document.body.dataset.functionModule;
  const name = document.body.dataset.functionName;
  const entry = window.DATAVIZ_MODULES[moduleSlug];
  const doc = functionDoc(moduleSlug, name);
  if (!entry || !doc) {
    target.innerHTML = `<div class="placeholder"><h1>Function Documentation</h1><p>This function page could not find its metadata.</p></div>`;
    return;
  }
  const related = (doc.related || []).map((relatedName) => functionCodeLink(moduleSlug, relatedName)).join(" ");
  target.innerHTML = html`
    <nav class="breadcrumbs">
      <a href="${siteLink("index.html")}">Docs</a>
      <span>/</span>
      <a href="${siteLink(entry.href)}">${entry.title}</a>
      <span>/</span>
      <span>${doc.submodule}</span>
    </nav>
    <section class="hero function-hero">
      <p class="eyebrow">${doc.mode} reference</p>
      <h1>${doc.name}</h1>
      <p class="lead">${doc.summary}</p>
      <div class="doc-meta">
        <span>${doc.moduleTitle}</span>
        <span>${doc.submodule}</span>
        <span>${doc.kind}</span>
        <span>${doc.source}</span>
      </div>
    </section>
    <h2>Signature</h2>
    <pre class="signature"><code>${doc.signature}</code></pre>
    <h2>Parameters</h2>
    ${doc.parameters.length ? `<table class="api-table param-table"><thead><tr><th>Name</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody>${doc.parameters.map((param) => `<tr><td><code>${param.name}</code></td><td><code>${param.type}</code></td><td>${param.required ? "Yes" : "No"}</td><td>${param.description}</td></tr>`).join("")}</tbody></table>` : `<p>This entry does not expose public call parameters.</p>`}
    <h2>Returns</h2>
    <p>${doc.returns}</p>
    <h2>Errors</h2>
    <p>${doc.errors}</p>
    <h2>Usage Example</h2>
    <pre><code>${doc.example}</code></pre>
    <h2>Additional Explanation</h2>
    <p>${doc.explanation}</p>
    <div class="callout">
      <strong>Implementation source:</strong> <code>${doc.source}</code>
    </div>
    ${related ? `<h2>Related Entries</h2><p class="related-links">${related}</p>` : ""}
    <p class="footer-link"><a href="${siteLink(entry.href)}">Back to ${entry.title} module</a></p>`;
}

function initSearch() {
  const input = document.querySelector("[data-search]");
  if (!input) return;
  input.addEventListener("input", () => {
    const q = input.value.toLowerCase().trim();
    const nav = document.querySelector("[data-nav]");
    if (!nav) return;
    if (!q) {
      nav.querySelectorAll("li").forEach((li) => (li.style.display = ""));
      nav.querySelectorAll("details").forEach((d) => d.removeAttribute("data-search-open"));
      return;
    }
    nav.querySelectorAll("li").forEach((li) => (li.style.display = "none"));
    nav.querySelectorAll(".nav-list a, .nav-list summary").forEach((el) => {
      if (!el.textContent.toLowerCase().includes(q)) return;
      let node = el.closest("li");
      while (node) {
        node.style.display = "";
        const det = node.parentElement?.closest("details");
        if (det) {
          det.open = true;
          det.setAttribute("data-search-open", "1");
          node = det.closest("li");
        } else {
          node = null;
        }
      }
    });
  });
}

renderNav();
renderModulePage();
renderApiIndex();
renderFunctionPage();
initSearch();
