---
title: KerberosPrincipal.KerberosPrincipal()
permalink: Java/KerberosPrincipal/KerberosPrincipal
date: 2021-01-04
key: JavaJava.K.KerberosPrincipal
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KerberosPrincipal.constructores valor="KerberosPrincipal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public KerberosPrincipal(String name)
public KerberosPrincipal(String name, int nameType)
~~~

## Parámetros
* **int nameType**,  {% include w3api/param_description.html metodo=_data parametro="int nameType" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[KerberosPrincipal](/Java/KerberosPrincipal/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KerberosPrincipal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
