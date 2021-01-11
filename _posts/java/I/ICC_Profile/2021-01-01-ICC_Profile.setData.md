---
title: ICC_Profile.setData()
permalink: Java/ICC_Profile/setData
date: 2021-01-11
key: JavaJava.I.ICC_Profile
category: java
tags: ['java se', 'java.awt.color', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ICC_Profile.metodos valor="setData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setData(int tagSignature, byte[] tagData)
~~~

## Parámetros
* **int tagSignature**,  {% include w3api/param_description.html metodo=_dato parametro="int tagSignature" %}
* **byte[] tagData**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] tagData" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ICC_Profile](/Java/ICC_Profile/)

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
