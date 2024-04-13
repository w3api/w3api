---
title: CheckboxMenuItem.CheckboxMenuItem()
permalink: /Java/CheckboxMenuItem/CheckboxMenuItem/
date: 2021-01-11
key: Java.C.CheckboxMenuItem
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckboxMenuItem.constructores valor="CheckboxMenuItem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CheckboxMenuItem() throws HeadlessException
public CheckboxMenuItem(String label) throws HeadlessException
public CheckboxMenuItem(String label, boolean state) throws HeadlessException
~~~

## Parámetros
* **boolean state**,  {% include w3api/param_description.html metodo=_dato parametro="boolean state" %}
* **String label**,  {% include w3api/param_description.html metodo=_dato parametro="String label" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/)

## Clase Padre
[CheckboxMenuItem](/Java/CheckboxMenuItem/)

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
