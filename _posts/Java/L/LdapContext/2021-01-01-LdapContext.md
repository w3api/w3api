---
title: LdapContext
permalink: /Java/LdapContext/
date: 2021-01-11
key: Java.L.LdapContext
category: Java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LdapContext.description }}

## Sintaxis
~~~java
public interface LdapContext extends DirContext
~~~

## Campos
* [CONTROL_FACTORIES](/Java/LdapContext/CONTROL_FACTORIES/)

## Métodos
* [extendedOperation()](/Java/LdapContext/extendedOperation/)
* [getConnectControls()](/Java/LdapContext/getConnectControls/)
* [getRequestControls()](/Java/LdapContext/getRequestControls/)
* [getResponseControls()](/Java/LdapContext/getResponseControls/)
* [newInstance()](/Java/LdapContext/newInstance/)
* [reconnect()](/Java/LdapContext/reconnect/)
* [setRequestControls()](/Java/LdapContext/setRequestControls/)

## Ejemplo
~~~java
{{ site.data.Java.L.LdapContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LdapContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
