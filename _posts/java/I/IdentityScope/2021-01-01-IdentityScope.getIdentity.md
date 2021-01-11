---
title: IdentityScope.getIdentity()
permalink: Java/IdentityScope/getIdentity
date: 2021-01-11
key: JavaJava.I.IdentityScope
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IdentityScope.metodos valor="getIdentity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Identity getIdentity(String name)
public Identity getIdentity(Principal principal)
public abstract Identity getIdentity(PublicKey key)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **PublicKey key**,  {% include w3api/param_description.html metodo=_dato parametro="PublicKey key" %}
* **Principal principal**,  {% include w3api/param_description.html metodo=_dato parametro="Principal principal" %}

## Clase Padre
[IdentityScope](/Java/IdentityScope/)

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
