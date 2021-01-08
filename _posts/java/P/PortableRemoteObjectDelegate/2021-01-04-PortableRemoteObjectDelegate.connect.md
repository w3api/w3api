---
title: PortableRemoteObjectDelegate.connect()
permalink: Java/PortableRemoteObjectDelegate/connect
date: 2021-01-04
key: JavaJava.P.PortableRemoteObjectDelegate
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PortableRemoteObjectDelegate.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void connect(Remote target, Remote source) throws RemoteException
~~~

## Parámetros
* **Remote target**,  {% include w3api/param_description.html metodo=_data parametro="Remote target" %}
* **Remote source**,  {% include w3api/param_description.html metodo=_data parametro="Remote source" %}

## Excepciones
[RemoteException](/Java/RemoteException/)

## Clase Padre
[PortableRemoteObjectDelegate](/Java/PortableRemoteObjectDelegate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PortableRemoteObjectDelegate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
