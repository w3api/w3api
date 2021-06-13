---
title: Transform.affine()
permalink: /Java/Transform-javafx-scene-transform/affine/
date: 2021-01-11
key: Java.T.Transform-javafx-scene-transform
category: Java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="affine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Affine affine(double mxx, double myx, double mxy, double myy, double tx, double ty)
public static Affine affine(double mxx, double mxy, double mxz, double tx, double myx, double myy, double myz, double ty, double mzx, double mzy, double mzz, double tz)
~~~

## Parámetros
* **double myy**,  {% include w3api/param_description.html metodo=_dato parametro="double myy" %}
* **double tx**,  {% include w3api/param_description.html metodo=_dato parametro="double tx" %}
* **double ty**,  {% include w3api/param_description.html metodo=_dato parametro="double ty" %}
* **double myz**,  {% include w3api/param_description.html metodo=_dato parametro="double myz" %}
* **double mxx**,  {% include w3api/param_description.html metodo=_dato parametro="double mxx" %}
* **double mzx**,  {% include w3api/param_description.html metodo=_dato parametro="double mzx" %}
* **double tz**,  {% include w3api/param_description.html metodo=_dato parametro="double tz" %}
* **double mxy**,  {% include w3api/param_description.html metodo=_dato parametro="double mxy" %}
* **double mxz**,  {% include w3api/param_description.html metodo=_dato parametro="double mxz" %}
* **double mzy**,  {% include w3api/param_description.html metodo=_dato parametro="double mzy" %}
* **double mzz**,  {% include w3api/param_description.html metodo=_dato parametro="double mzz" %}
* **double myx**,  {% include w3api/param_description.html metodo=_dato parametro="double myx" %}

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
