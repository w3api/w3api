---
title: FontMetrics.getLineMetrics()
permalink: /Java/FontMetrics/getLineMetrics/
date: 2021-01-11
key: Java.F.FontMetrics
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FontMetrics.metodos valor="getLineMetrics" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LineMetrics getLineMetrics(char[] chars, int beginIndex, int limit, Graphics context)
public LineMetrics getLineMetrics(String str, int beginIndex, int limit, Graphics context)
public LineMetrics getLineMetrics(String str, Graphics context)
public LineMetrics getLineMetrics(CharacterIterator ci, int beginIndex, int limit, Graphics context)
~~~

## Parámetros
* **CharacterIterator ci**,  {% include w3api/param_description.html metodo=_dato parametro="CharacterIterator ci" %}
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int beginIndex" %}
* **int limit**,  {% include w3api/param_description.html metodo=_dato parametro="int limit" %}
* **char[] chars**,  {% include w3api/param_description.html metodo=_dato parametro="char[] chars" %}
* **Graphics context**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics context" %}

## Clase Padre
[FontMetrics](/Java/FontMetrics/)

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
