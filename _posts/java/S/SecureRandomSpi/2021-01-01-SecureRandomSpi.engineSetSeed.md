---
title: SecureRandomSpi.engineSetSeed()
permalink: Java/SecureRandomSpi/engineSetSeed
date: 2021-01-11
key: JavaJava.S.SecureRandomSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandomSpi.metodos valor="engineSetSeed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineSetSeed(byte[] seed)
~~~

## Parámetros
* **byte[] seed**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] seed" %}

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
