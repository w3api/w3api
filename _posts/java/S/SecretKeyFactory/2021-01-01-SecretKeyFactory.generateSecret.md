---
title: SecretKeyFactory.generateSecret()
permalink: Java/SecretKeyFactory/generateSecret
date: 2021-01-11
key: JavaJava.S.SecretKeyFactory
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecretKeyFactory.metodos valor="generateSecret" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final SecretKey generateSecret(KeySpec keySpec) throws InvalidKeySpecException
~~~

## Parámetros
* **KeySpec keySpec**,  {% include w3api/param_description.html metodo=_dato parametro="KeySpec keySpec" %}

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
