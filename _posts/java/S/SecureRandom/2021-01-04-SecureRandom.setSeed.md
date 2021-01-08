---
title: SecureRandom.setSeed()
permalink: Java/SecureRandom/setSeed
date: 2021-01-04
key: JavaJava.S.SecureRandom
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandom.metodos valor="setSeed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSeed(byte[] seed)
public void setSeed(long seed)
~~~

## Parámetros
* **long seed**,  {% include w3api/param_description.html metodo=_data parametro="long seed" %}
* **byte[] seed**,  {% include w3api/param_description.html metodo=_data parametro="byte[] seed" %}

## Clase Padre
[SecureRandom](/Java/SecureRandom/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureRandom.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
