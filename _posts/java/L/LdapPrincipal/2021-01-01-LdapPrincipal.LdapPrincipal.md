---
title: LdapPrincipal.LdapPrincipal()
permalink: Java/LdapPrincipal/LdapPrincipal
date: 2021-01-11
key: Java.L.LdapPrincipal
category: java
tags: ['java se', 'com.sun.security.auth', 'jdk.security.auth', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LdapPrincipal.constructores valor="LdapPrincipal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LdapPrincipal(String name) throws InvalidNameException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[InvalidNameException](/Java/InvalidNameException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LdapPrincipal](/Java/LdapPrincipal/)

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
