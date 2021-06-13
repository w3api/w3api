---
title: SecureRandom.SecureRandom()
permalink: /Java/SecureRandom/SecureRandom/
date: 2021-01-11
key: Java.S.SecureRandom
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandom.constructores valor="SecureRandom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SecureRandom()
public SecureRandom(byte[] seed)
protected SecureRandom(SecureRandomSpi secureRandomSpi, Provider provider)
~~~

## Parámetros
* **byte[] seed**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] seed" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **SecureRandomSpi secureRandomSpi**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandomSpi secureRandomSpi" %}

## Clase Padre
[SecureRandom](/Java/SecureRandom/)

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
