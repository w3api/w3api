---
title: InitialLdapContext.InitialLdapContext()
permalink: Java/InitialLdapContext/InitialLdapContext
date: 2021-01-04
key: JavaJava.I.InitialLdapContext
category: java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InitialLdapContext.constructores valor="InitialLdapContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InitialLdapContext() throws NamingException
public InitialLdapContext(Hashtable<?,?> environment, Control[] connCtls) throws NamingException
~~~

## Parámetros
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_data parametro="Hashtable<?" %}
* **Control[] connCtls**,  {% include w3api/param_description.html metodo=_data parametro="Control[] connCtls" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_data parametro="?> environment" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[InitialLdapContext](/Java/InitialLdapContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InitialLdapContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
