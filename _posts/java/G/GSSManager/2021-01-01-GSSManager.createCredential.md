---
title: GSSManager.createCredential()
permalink: Java/GSSManager/createCredential
date: 2021-01-11
key: JavaJava.G.GSSManager
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSManager.metodos valor="createCredential" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract GSSCredential createCredential(int usage) throws GSSException
public abstract GSSCredential createCredential(GSSName name, int lifetime, Oid[] mechs, int usage) throws GSSException
public abstract GSSCredential createCredential(GSSName name, int lifetime, Oid mech, int usage) throws GSSException
~~~

## Parámetros
* **int lifetime**,  {% include w3api/param_description.html metodo=_dato parametro="int lifetime" %}
* **Oid[] mechs**,  {% include w3api/param_description.html metodo=_dato parametro="Oid[] mechs" %}
* **Oid mech**,  {% include w3api/param_description.html metodo=_dato parametro="Oid mech" %}
* **int usage**,  {% include w3api/param_description.html metodo=_dato parametro="int usage" %}
* **GSSName name**,  {% include w3api/param_description.html metodo=_dato parametro="GSSName name" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[GSSManager](/Java/GSSManager/)

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
