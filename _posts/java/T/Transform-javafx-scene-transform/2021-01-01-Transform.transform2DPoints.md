---
title: Transform.transform2DPoints()
permalink: /Java/Transform-javafx-scene-transform/transform2DPoints/
date: 2021-01-11
key: Java.T.Transform-javafx-scene-transform
category: Java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="transform2DPoints" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void transform2DPoints(double[] srcPts, int srcOff, double[] dstPts, int dstOff, int numPts)
~~~

## Parámetros
* **int srcOff**,  {% include w3api/param_description.html metodo=_dato parametro="int srcOff" %}
* **double[] srcPts**,  {% include w3api/param_description.html metodo=_dato parametro="double[] srcPts" %}
* **int dstOff**,  {% include w3api/param_description.html metodo=_dato parametro="int dstOff" %}
* **double[] dstPts**,  {% include w3api/param_description.html metodo=_dato parametro="double[] dstPts" %}
* **int numPts**,  {% include w3api/param_description.html metodo=_dato parametro="int numPts" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Transform](/Java/Transform-javafx-scene-transform/)

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
