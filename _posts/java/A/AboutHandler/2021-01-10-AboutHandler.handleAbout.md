---
title: AboutHandler.handleAbout()
permalink: Java/AboutHandler/handleAbout
date: 2021-01-10
key: JavaJava.A.AboutHandler
category: java
tags: ['java se', 'java.awt.desktop', 'java.desktop', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AboutHandler.metodos valor="handleAbout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void handleAbout(AboutEvent e)
~~~

## Parámetros
* **AboutEvent e**,  {% include w3api/param_description.html metodo=_dato parametro="AboutEvent e" %}

## Clase Padre
[AboutHandler](/Java/AboutHandler/)

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
