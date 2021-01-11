---
title: ClassLoader.definePackage()
permalink: Java/ClassLoader/definePackage
date: 2021-01-11
key: JavaJava.C.ClassLoader
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="definePackage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Package definePackage(String name, String specTitle, String specVersion, String specVendor, String implTitle, String implVersion, String implVendor, URL sealBase)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String specVersion**,  {% include w3api/param_description.html metodo=_dato parametro="String specVersion" %}
* **String implVersion**,  {% include w3api/param_description.html metodo=_dato parametro="String implVersion" %}
* **String specTitle**,  {% include w3api/param_description.html metodo=_dato parametro="String specTitle" %}
* **String implVendor**,  {% include w3api/param_description.html metodo=_dato parametro="String implVendor" %}
* **String specVendor**,  {% include w3api/param_description.html metodo=_dato parametro="String specVendor" %}
* **String implTitle**,  {% include w3api/param_description.html metodo=_dato parametro="String implTitle" %}
* **URL sealBase**,  {% include w3api/param_description.html metodo=_dato parametro="URL sealBase" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ClassLoader](/Java/ClassLoader/)

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
