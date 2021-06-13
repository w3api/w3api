---
title: LdapContext.extendedOperation()
permalink: Java/LdapContext/extendedOperation
date: 2021-01-11
key: Java.L.LdapContext
category: java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LdapContext.metodos valor="extendedOperation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ExtendedResponse extendedOperation(ExtendedRequest request) throws NamingException
~~~

## Parámetros
* **ExtendedRequest request**,  {% include w3api/param_description.html metodo=_dato parametro="ExtendedRequest request" %}

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
