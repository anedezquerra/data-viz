# Parameter Extension Template for Remaining Chart Functions

This template shows the standardized parameter pattern applied across all chart functions.

## Completed Modules (57% - 17/30 functions)
✅ **Univariate** (4/4): histogram, density, box_plot, violin_plot  
✅ **Bivariate** (3/3): scatter, line, correlation  
✅ **Multivariate** (3/3): pairplot, heatmap, parallel  
✅ **EDA** (3/3): missing_data, distribution, class_dist  
✅ **Regression** (3/3): residual, prediction, learning  
✅ **Classification** (1/3): confusion_matrix ✓ (ROC & PR_curve pending)

## Remaining Modules (13 functions - 43%)
- **Classification** (2/3): roc.py, pr_curve.py
- **Clustering** (0/3): scatter_clusters.py, elbow.py, dendrogram.py
- **XAI** (0/3): feature_imp.py, shap.py, partial_dep.py
- **SPC** (0/2): control.py, x_range.py

## Standard Parameter Template

### Static Function Pattern
```python
def chart_name_static(
    data: ...,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    color: Optional[str] = None,
    alpha: float = 0.7,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    **kwargs
) -> plt.Axes:
    """Complete docstring..."""
    if title is None:
        title = "Chart Title"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        # Implementation specific to chart type
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        # Grid
        if grid:
            ax.grid(True, alpha=grid_alpha)
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax
```

### Interactive Function Pattern
```python
def chart_name_interactive(
    data: ...,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    showlegend: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    **kwargs
) -> go.Figure:
    """Complete docstring..."""
    if title is None:
        title = "Chart Title"
    if color is None:
        color = marker_color
    
    # Implementation specific to chart type
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
```

## Common Parameters by Category

### Display Parameters
- `title: Optional[str] = None` - Chart title
- `xlabel`, `ylabel` - Axis labels

### Layout Parameters
- `figsize: Tuple[int, int] = (10, 6)` - Figure size 
- `height: int = 600`, `width: int = 1000` - Plotly dimensions

### Appearance Parameters
- `color`, `marker_color` - Primary color
- `alpha: float = 0.7` - Transparency
- `edgecolor: str = 'black'` - Edge/border color
- `linewidth: float = 1.0` - Line/border width

### Font Parameters
- `font_size: int = 10` - Default font size
- `title_size: int = 14` - Title font size
- `label_size: int = 11` - Axis label font size

### Style Parameters
- `theme: str = 'default'` - 'default', 'dark', 'minimal'
- `style: str = 'default'` - matplotlib style
- `template: str = 'plotly'` - Plotly template
- `dpi: int = 100` - Figure DPI

### Grid/Legend Parameters
- `grid: bool = True` - Show grid
- `grid_alpha: float = 0.3` - Grid transparency
- `showlegend: bool = True` - Show legend (interactive)

### Hover/Interaction
- `hovermode: str = 'closest'` - Hover mode (interactive)

## Files Needing Update

Use the template above for these files:

### Classification (2 files)
- `dataviz/classification/roc.py` - Add: threshold_markers, line_dash params
- `dataviz/classification/pr_curve.py` - Add: threshold_markers, confidence_band params

### Clustering (3 files)
- `dataviz/clustering/scatter_clusters.py` - Add: cluster_colors, marker_shapes params
- `dataviz/clustering/elbow.py` - Add: knee_marker, line_style params  
- `dataviz/clustering/dendrogram.py` - Add: color_threshold, orientation params

### XAI (3 files)
- `dataviz/xai/feature_imp.py` - Add: sort_order, confidence_interval params
- `dataviz/xai/shap.py` - Add: color_positive, color_negative params
- `dataviz/xai/partial_dep.py` - Add: confidence_region, scaling params

### SPC (2 files)
- `dataviz/spc/control.py` - Add: control_limit_style, sample_marker params
- `dataviz/spc/x_range.py` - Add: subgroup_markers, reference_line_style params

## Application Strategy

1. **Copy template pattern** for each chart type
2. **Adapt chart-specific parameters** (e.g., threshold_markers for ROC)
3. **Maintain docstring consistency** with "Parameters" section
4. **Keep **kwargs** for backward compatibility
5. **Apply to both _static and _interactive versions**

## Example: ROC Curve Extension

See [roc.py enhancement pattern]:
- Add: `threshold_markers: bool = False`
- Add: `line_dash: str = 'solid'`
- Add: `line_width: float = 2.0`
- Implement threshold markers at decision boundaries
- Update both matplotlib and plotly versions

## Validation

After updates, run:
```bash
pytest tests/test_core.py -v
```

Ensure all functions accept the new parameters with sensible defaults!
