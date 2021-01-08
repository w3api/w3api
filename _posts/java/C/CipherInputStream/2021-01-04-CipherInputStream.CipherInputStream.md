---
title: CipherInputStream.CipherInputStream()
permalink: Java/CipherInputStream/CipherInputStream
date: 2021-01-04
key: JavaJava.C.CipherInputStream
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CipherInputStream.constructores valor="CipherInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CipherInputStream(InputStream is)
public CipherInputStream(InputStream is, Cipher c)
~~~

## Parámetros
* **InputStream is**,  {% include w3api/param_description.html metodo=_data parametro="InputStream is" %}
* **Cipher c**,  {% include w3api/param_description.html metodo=_data parametro="Cipher c" %}

## Clase Padre
[CipherInputStream](/Java/CipherInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CipherInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
