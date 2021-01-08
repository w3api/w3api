---
title: GraphicsContext.setTransform()
permalink: Java/GraphicsContext/setTransform
date: 2021-01-04
key: JavaJava.G.GraphicsContext
category: java
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
* **Affine xform**,  {% include w3api/param_description.html metodo=_data parametro="Affine xform" %}
* **double myt**,  {% include w3api/param_description.html metodo=_data parametro="double myt" %}
* **double mxy**,  {% include w3api/param_description.html metodo=_data parametro="double mxy" %}
* **double mxx**,  {% include w3api/param_description.html metodo=_data parametro="double mxx" %}
* **double mxt**,  {% include w3api/param_description.html metodo=_data parametro="double mxt" %}
* **double myx**,  {% include w3api/param_description.html metodo=_data parametro="double myx" %}
* **double myy**,  {% include w3api/param_description.html metodo=_data parametro="double myy" %}

## Clase Padre
[GraphicsContext](/Java/GraphicsContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GraphicsContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
