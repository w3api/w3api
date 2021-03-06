---
title: KeyGenerator.KeyGenerator()
permalink: /Java/KeyGenerator/KeyGenerator/
date: 2021-01-11
key: Java.K.KeyGenerator
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyGenerator.constructores valor="KeyGenerator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected KeyGenerator(KeyGeneratorSpi keyGenSpi, Provider provider, String algorithm)
~~~

## Parámetros
* **KeyGeneratorSpi keyGenSpi**,  {% include w3api/param_description.html metodo=_dato parametro="KeyGeneratorSpi keyGenSpi" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}

## Clase Padre
[KeyGenerator](/Java/KeyGenerator/)

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
