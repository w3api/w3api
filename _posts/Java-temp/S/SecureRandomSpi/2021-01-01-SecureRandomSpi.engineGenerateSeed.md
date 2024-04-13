---
title: SecureRandomSpi.engineGenerateSeed()
permalink: /Java/SecureRandomSpi/engineGenerateSeed/
date: 2021-01-11
key: Java.S.SecureRandomSpi
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandomSpi.metodos valor="engineGenerateSeed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract byte[] engineGenerateSeed(int numBytes)
~~~

## Parámetros
* **int numBytes**,  {% include w3api/param_description.html metodo=_dato parametro="int numBytes" %}

## Clase Padre
[SecureRandomSpi](/Java/SecureRandomSpi/)

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
