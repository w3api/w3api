---
title: StringContent.getString()
permalink: /Java/StringContent/getString/
date: 2021-01-11
key: Java.S.StringContent
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringContent.metodos valor="getString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getString(int where, int len) throws BadLocationException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int where**,  {% include w3api/param_description.html metodo=_dato parametro="int where" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[StringContent](/Java/StringContent/)

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
