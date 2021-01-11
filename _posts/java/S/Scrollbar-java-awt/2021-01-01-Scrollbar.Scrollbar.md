---
title: Scrollbar.Scrollbar()
permalink: Java/Scrollbar-java-awt/Scrollbar
date: 2021-01-11
key: JavaJava.S.Scrollbar-java-awt
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Scrollbar-java-awt.constructores valor="Scrollbar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Scrollbar() throws HeadlessException
public Scrollbar(int orientation) throws HeadlessException
public Scrollbar(int orientation, int value, int visible, int minimum, int maximum) throws HeadlessException
~~~

## Parámetros
* **int value**,  {% include w3api/param_description.html metodo=_dato parametro="int value" %}
* **int minimum**,  {% include w3api/param_description.html metodo=_dato parametro="int minimum" %}
* **int maximum**,  {% include w3api/param_description.html metodo=_dato parametro="int maximum" %}
* **int visible**,  {% include w3api/param_description.html metodo=_dato parametro="int visible" %}
* **int orientation**,  {% include w3api/param_description.html metodo=_dato parametro="int orientation" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Scrollbar](/Java/Scrollbar-java-awt/)

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
