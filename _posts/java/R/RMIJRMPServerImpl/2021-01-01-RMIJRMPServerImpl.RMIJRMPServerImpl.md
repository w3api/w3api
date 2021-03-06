---
title: RMIJRMPServerImpl.RMIJRMPServerImpl()
permalink: /Java/RMIJRMPServerImpl/RMIJRMPServerImpl/
date: 2021-01-11
key: Java.R.RMIJRMPServerImpl
category: Java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIJRMPServerImpl.constructores valor="RMIJRMPServerImpl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RMIJRMPServerImpl(int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf, Map<String,?> env) throws IOException
~~~

## Parámetros
* **RMIClientSocketFactory csf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIClientSocketFactory csf" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **RMIServerSocketFactory ssf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIServerSocketFactory ssf" %}
* **?&gt; env**,  {% include w3api/param_description.html metodo=_dato parametro="?> env" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[RMIJRMPServerImpl](/Java/RMIJRMPServerImpl/)

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
