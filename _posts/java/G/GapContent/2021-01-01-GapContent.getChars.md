---
title: GapContent.getChars()
permalink: /Java/GapContent/getChars/
date: 2021-01-11
key: Java.G.GapContent
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GapContent.metodos valor="getChars" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void getChars(int where, int len, Segment chars) throws BadLocationException
~~~

## Parámetros
* **Segment chars**,  {% include w3api/param_description.html metodo=_dato parametro="Segment chars" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int where**,  {% include w3api/param_description.html metodo=_dato parametro="int where" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[GapContent](/Java/GapContent/)

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
