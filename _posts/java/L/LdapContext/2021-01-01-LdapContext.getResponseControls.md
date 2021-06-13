---
title: LdapContext.getResponseControls()
permalink: /Java/LdapContext/getResponseControls/
date: 2021-01-11
key: Java.L.LdapContext
category: Java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LdapContext.metodos valor="getResponseControls" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Control[] getResponseControls() throws NamingException
~~~

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[LdapContext](/Java/LdapContext/)

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
