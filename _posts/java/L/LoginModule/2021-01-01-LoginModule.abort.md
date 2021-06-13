---
title: LoginModule.abort()
permalink: Java/LoginModule/abort
date: 2021-01-11
key: Java.L.LoginModule
category: java
tags: ['java se', 'javax.security.auth.spi', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LoginModule.metodos valor="abort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean abort() throws LoginException
~~~

## Excepciones
[LoginException](/Java/LoginException/)

## Clase Padre
[LoginModule](/Java/LoginModule/)

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
