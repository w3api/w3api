---
title: ClassLoader.definePackage()
permalink: Java/ClassLoader/definePackage
date: 2021-01-04
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
* **String implVendor**,  {% include w3api/param_description.html metodo=_data parametro="String implVendor" %}
* **String specTitle**,  {% include w3api/param_description.html metodo=_data parametro="String specTitle" %}
* **String specVendor**,  {% include w3api/param_description.html metodo=_data parametro="String specVendor" %}
* **URL sealBase**,  {% include w3api/param_description.html metodo=_data parametro="URL sealBase" %}
* **String implVersion**,  {% include w3api/param_description.html metodo=_data parametro="String implVersion" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String specVersion**,  {% include w3api/param_description.html metodo=_data parametro="String specVersion" %}
* **String implTitle**,  {% include w3api/param_description.html metodo=_data parametro="String implTitle" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ClassLoader](/Java/ClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
