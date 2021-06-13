---
title: RepaintManager.addDirtyRegion()
permalink: Java/RepaintManager/addDirtyRegion
date: 2021-01-11
key: Java.R.RepaintManager
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RepaintManager.metodos valor="addDirtyRegion" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9") public void addDirtyRegion(Applet applet, int x, int y, int w, int h)
public void addDirtyRegion(Window window, int x, int y, int w, int h)
public void addDirtyRegion(JComponent c, int x, int y, int w, int h)
~~~

## Parámetros
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **Window window**,  {% include w3api/param_description.html metodo=_dato parametro="Window window" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Applet applet**,  {% include w3api/param_description.html metodo=_dato parametro="Applet applet" %}

## Clase Padre
[RepaintManager](/Java/RepaintManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
