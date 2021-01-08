---
title: RegistryHandler.registryStub()
permalink: Java/RegistryHandler/registryStub
date: 2021-01-04
key: JavaJava.R.RegistryHandler
category: java
tags: ['java se', 'java.rmi.registry', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RegistryHandler.metodos valor="registryStub" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated Registry registryStub(String host, int port) throws RemoteException, UnknownHostException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **String host**,  {% include w3api/param_description.html metodo=_data parametro="String host" %}

## Excepciones
[UnknownHostException](/Java/UnknownHostException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[RegistryHandler](/Java/RegistryHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RegistryHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
