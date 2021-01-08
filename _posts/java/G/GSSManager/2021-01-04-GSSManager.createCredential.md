---
title: GSSManager.createCredential()
permalink: Java/GSSManager/createCredential
date: 2021-01-04
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
* **GSSName name**,  {% include w3api/param_description.html metodo=_data parametro="GSSName name" %}
* **int usage**,  {% include w3api/param_description.html metodo=_data parametro="int usage" %}
* **Oid[] mechs**,  {% include w3api/param_description.html metodo=_data parametro="Oid[] mechs" %}
* **Oid mech**,  {% include w3api/param_description.html metodo=_data parametro="Oid mech" %}
* **int lifetime**,  {% include w3api/param_description.html metodo=_data parametro="int lifetime" %}

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
{%- for _ldc in site.data.Java.G.GSSManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
