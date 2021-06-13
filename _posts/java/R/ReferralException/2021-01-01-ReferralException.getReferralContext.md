---
title: ReferralException.getReferralContext()
permalink: Java/ReferralException/getReferralContext
date: 2021-01-11
key: Java.R.ReferralException
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReferralException.metodos valor="getReferralContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Context getReferralContext() throws NamingException
public abstract Context getReferralContext(Hashtable<?,?> env) throws NamingException
~~~

## Parámetros
* **?&gt; env**,  {% include w3api/param_description.html metodo=_dato parametro="?> env" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[ReferralException](/Java/ReferralException/)

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
