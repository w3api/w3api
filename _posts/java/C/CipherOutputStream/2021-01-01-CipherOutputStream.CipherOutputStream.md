---
title: CipherOutputStream.CipherOutputStream()
permalink: /Java/CipherOutputStream/CipherOutputStream/
date: 2021-01-11
key: Java.C.CipherOutputStream
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CipherOutputStream.constructores valor="CipherOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CipherOutputStream(OutputStream os)
public CipherOutputStream(OutputStream os, Cipher c)
~~~

## Parámetros
* **Cipher c**,  {% include w3api/param_description.html metodo=_dato parametro="Cipher c" %}
* **OutputStream os**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream os" %}

## Clase Padre
[CipherOutputStream](/Java/CipherOutputStream/)

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
