---
title: JTextArea.replaceRange()
permalink: Java/JTextArea/replaceRange
date: 2021-01-04
key: JavaJava.J.JTextArea
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextArea.metodos valor="replaceRange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void replaceRange(String str, int start, int end)
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **String str**,  {% include w3api/param_description.html metodo=_data parametro="String str" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}

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
{%- for _ldc in site.data.Java.J.JTextArea.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
