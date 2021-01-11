---
title: LdapReferralException.getReferralContext()
permalink: Java/LdapReferralException/getReferralContext
date: 2021-01-11
key: JavaJava.L.LdapReferralException
category: java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LdapReferralException.metodos valor="getReferralContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Context getReferralContext() throws NamingException
public abstract Context getReferralContext(Hashtable<?,?> env) throws NamingException
public abstract Context getReferralContext(Hashtable<?,?> env, Control[] reqCtls) throws NamingException
~~~

## Parámetros
* **Control[] reqCtls**,  {% include w3api/param_description.html metodo=_dato parametro="Control[] reqCtls" %}
* **?&gt; env**,  {% include w3api/param_description.html metodo=_dato parametro="?> env" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[LdapReferralException](/Java/LdapReferralException/)

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
