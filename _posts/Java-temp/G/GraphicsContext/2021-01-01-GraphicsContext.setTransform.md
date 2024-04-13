---
title: GraphicsContext.setTransform()
permalink: /Java/GraphicsContext/setTransform/
date: 2021-01-11
key: Java.G.GraphicsContext
category: Java
tags: ['java se', 'javafx.scene.canvas', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GraphicsContext.metodos valor="setTransform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTransform(double mxx, double myx, double mxy, double myy, double mxt, double myt)
public void setTransform(Affine xform)
~~~

## Parámetros
* **Affine xform**,  {% include w3api/param_description.html metodo=_dato parametro="Affine xform" %}
* **double myy**,  {% include w3api/param_description.html metodo=_dato parametro="double myy" %}
* **double mxt**,  {% include w3api/param_description.html metodo=_dato parametro="double mxt" %}
* **double mxx**,  {% include w3api/param_description.html metodo=_dato parametro="double mxx" %}
* **double myt**,  {% include w3api/param_description.html metodo=_dato parametro="double myt" %}
* **double mxy**,  {% include w3api/param_description.html metodo=_dato parametro="double mxy" %}
* **double myx**,  {% include w3api/param_description.html metodo=_dato parametro="double myx" %}

## Clase Padre
[GraphicsContext](/Java/GraphicsContext/)

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
