---
title: CodeSource.CodeSource()
permalink: /Java/CodeSource/CodeSource/
date: 2021-01-11
key: Java.C.CodeSource
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CodeSource.constructores valor="CodeSource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CodeSource(URL url, Certificate[] certs)
public CodeSource(URL url, CodeSigner[] signers)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **Certificate[] certs**,  {% include w3api/param_description.html metodo=_dato parametro="Certificate[] certs" %}
* **CodeSigner[] signers**,  {% include w3api/param_description.html metodo=_dato parametro="CodeSigner[] signers" %}

## Clase Padre
[CodeSource](/Java/CodeSource/)

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
