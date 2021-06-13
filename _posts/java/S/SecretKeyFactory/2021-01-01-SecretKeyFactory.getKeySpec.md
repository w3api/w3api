---
title: SecretKeyFactory.getKeySpec()
permalink: /Java/SecretKeyFactory/getKeySpec/
date: 2021-01-11
key: Java.S.SecretKeyFactory
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecretKeyFactory.metodos valor="getKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final KeySpec getKeySpec(SecretKey key, Class<?> keySpec) throws InvalidKeySpecException
~~~

## Parámetros
* **Class&lt;?&gt; keySpec**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> keySpec" %}
* **SecretKey key**,  {% include w3api/param_description.html metodo=_dato parametro="SecretKey key" %}

## Excepciones
[InvalidKeySpecException](/Java/InvalidKeySpecException/)

## Clase Padre
[SecretKeyFactory](/Java/SecretKeyFactory/)

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
