---
title: PrivateMLet.PrivateMLet()
permalink: Java/PrivateMLet/PrivateMLet
date: 2021-01-04
key: JavaJava.P.PrivateMLet
category: java
tags: ['java se', 'javax.management.loading', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrivateMLet.constructores valor="PrivateMLet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrivateMLet(URL[] urls, boolean delegateToCLR)
public PrivateMLet(URL[] urls, ClassLoader parent, boolean delegateToCLR)
public PrivateMLet(URL[] urls, ClassLoader parent, URLStreamHandlerFactory factory, boolean delegateToCLR)
~~~

## Parámetros
* **ClassLoader parent**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader parent" %}
* **URLStreamHandlerFactory factory**,  {% include w3api/param_description.html metodo=_data parametro="URLStreamHandlerFactory factory" %}
* **URL[] urls**,  {% include w3api/param_description.html metodo=_data parametro="URL[] urls" %}
* **boolean delegateToCLR**,  {% include w3api/param_description.html metodo=_data parametro="boolean delegateToCLR" %}

## Clase Padre
[PrivateMLet](/Java/PrivateMLet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrivateMLet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
