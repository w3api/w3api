---
title: ICC_Profile.getData()
permalink: /Java/ICC_Profile/getData/
date: 2021-01-11
key: Java.I.ICC_Profile
category: Java
tags: ['java se', 'java.awt.color', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ICC_Profile.metodos valor="getData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public byte[] getData()
public byte[] getData(int tagSignature)
~~~

## Parámetros
* **int tagSignature**,  {% include w3api/param_description.html metodo=_dato parametro="int tagSignature" %}

## Clase Padre
[ICC_Profile](/Java/ICC_Profile/)

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
