---
title: KerberosTicket.getSessionKey()
permalink: Java/KerberosTicket/getSessionKey
date: 2021-01-11
key: JavaJava.K.KerberosTicket
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KerberosTicket.metodos valor="getSessionKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final SecretKey getSessionKey()
~~~

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[KerberosTicket](/Java/KerberosTicket/)

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