---
title: JTextArea.insert()
permalink: Java/JTextArea/insert
date: 2021-01-11
key: JavaJava.J.JTextArea
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextArea.metodos valor="insert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insert(String str, int pos)
~~~

## Parámetros
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTextArea](/Java/JTextArea/)

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
