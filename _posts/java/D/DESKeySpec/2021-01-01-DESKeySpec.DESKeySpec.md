---
title: DESKeySpec.DESKeySpec()
permalink: /Java/DESKeySpec/DESKeySpec/
date: 2021-01-11
key: Java.D.DESKeySpec
category: Java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DESKeySpec.constructores valor="DESKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DESKeySpec(byte[] key) throws InvalidKeyException
public DESKeySpec(byte[] key, int offset) throws InvalidKeyException
~~~

## Parámetros
* **byte[] key**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] key" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DESKeySpec](/Java/DESKeySpec/)

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
