---
title: PhongMaterial.PhongMaterial()
permalink: Java/PhongMaterial/PhongMaterial
date: 2021-01-04
key: JavaJava.P.PhongMaterial
category: java
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
* **Image diffuseMap**,  {% include w3api/param_description.html metodo=_data parametro="Image diffuseMap" %}
* **Image selfIlluminationMap**,  {% include w3api/param_description.html metodo=_data parametro="Image selfIlluminationMap" %}
* **Image bumpMap**,  {% include w3api/param_description.html metodo=_data parametro="Image bumpMap" %}
* **Image specularMap**,  {% include w3api/param_description.html metodo=_data parametro="Image specularMap" %}
* **Color diffuseColor**,  {% include w3api/param_description.html metodo=_data parametro="Color diffuseColor" %}

## Clase Padre
[PhongMaterial](/Java/PhongMaterial/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PhongMaterial.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
