---
title: SecretKeyFactorySpi.engineGetKeySpec()
permalink: Java/SecretKeyFactorySpi/engineGetKeySpec
date: 2021-01-04
key: JavaJava.S.SecretKeyFactorySpi
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecretKeyFactorySpi.metodos valor="engineGetKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract KeySpec engineGetKeySpec(SecretKey key, Class<?> keySpec) throws InvalidKeySpecException
~~~

## Parámetros
* **Class&lt;?&gt; keySpec**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> keySpec" %}
* **SecretKey key**,  {% include w3api/param_description.html metodo=_data parametro="SecretKey key" %}

## Excepciones
[InvalidKeySpecException](/Java/InvalidKeySpecException/)

## Clase Padre
[SecretKeyFactorySpi](/Java/SecretKeyFactorySpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecretKeyFactorySpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
