---
title: JarSigner.getProperty()
permalink: /Java/JarSigner/getProperty/
date: 2021-01-11
key: Java.J.JarSigner
category: Java
tags: ['java se', 'jdk.security.jarsigner', 'jdk.jartool', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarSigner.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getProperty(String key)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[JarSigner](/Java/JarSigner/)

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
