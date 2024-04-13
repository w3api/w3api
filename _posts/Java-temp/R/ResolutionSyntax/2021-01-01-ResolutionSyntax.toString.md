---
title: ResolutionSyntax.toString()
permalink: /Java/ResolutionSyntax/toString/
date: 2021-01-11
key: Java.R.ResolutionSyntax
category: Java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResolutionSyntax.metodos valor="toString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String toString()
public String toString(int units, String unitsName)
~~~

## Parámetros
* **String unitsName**,  {% include w3api/param_description.html metodo=_dato parametro="String unitsName" %}
* **int units**,  {% include w3api/param_description.html metodo=_dato parametro="int units" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ResolutionSyntax](/Java/ResolutionSyntax/)

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
