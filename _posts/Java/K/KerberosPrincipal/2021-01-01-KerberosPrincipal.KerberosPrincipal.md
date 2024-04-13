---
title: KerberosPrincipal.KerberosPrincipal()
permalink: /Java/KerberosPrincipal/KerberosPrincipal/
date: 2021-01-11
key: Java.K.KerberosPrincipal
category: Java
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **int nameType**,  {% include w3api/param_description.html metodo=_dato parametro="int nameType" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
