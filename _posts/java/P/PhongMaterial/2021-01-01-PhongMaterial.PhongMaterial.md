---
title: PhongMaterial.PhongMaterial()
permalink: /Java/PhongMaterial/PhongMaterial/
date: 2021-01-11
key: Java.P.PhongMaterial
category: Java
tags: ['java se', 'javafx.scene.paint', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PhongMaterial.constructores valor="PhongMaterial" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PhongMaterial()
public PhongMaterial(Color diffuseColor)
public PhongMaterial(Color diffuseColor, Image diffuseMap, Image specularMap, Image bumpMap, Image selfIlluminationMap)
~~~

## Parámetros
* **Image bumpMap**,  {% include w3api/param_description.html metodo=_dato parametro="Image bumpMap" %}
* **Color diffuseColor**,  {% include w3api/param_description.html metodo=_dato parametro="Color diffuseColor" %}
* **Image specularMap**,  {% include w3api/param_description.html metodo=_dato parametro="Image specularMap" %}
* **Image diffuseMap**,  {% include w3api/param_description.html metodo=_dato parametro="Image diffuseMap" %}
* **Image selfIlluminationMap**,  {% include w3api/param_description.html metodo=_dato parametro="Image selfIlluminationMap" %}

## Clase Padre
[PhongMaterial](/Java/PhongMaterial/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
