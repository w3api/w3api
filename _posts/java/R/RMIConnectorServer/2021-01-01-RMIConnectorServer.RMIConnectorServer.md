---
title: RMIConnectorServer.RMIConnectorServer()
permalink: Java/RMIConnectorServer/RMIConnectorServer
date: 2021-01-11
key: JavaJava.R.RMIConnectorServer
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnectorServer.constructores valor="RMIConnectorServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RMIConnectorServer(JMXServiceURL url, Map<String,?> environment) throws IOException
public RMIConnectorServer(JMXServiceURL url, Map<String,?> environment, MBeanServer mbeanServer) throws IOException
public RMIConnectorServer(JMXServiceURL url, Map<String,?> environment, RMIServerImpl rmiServerImpl, MBeanServer mbeanServer) throws IOException
~~~

## Parámetros
* **JMXServiceURL url**,  {% include w3api/param_description.html metodo=_dato parametro="JMXServiceURL url" %}
* **RMIServerImpl rmiServerImpl**,  {% include w3api/param_description.html metodo=_dato parametro="RMIServerImpl rmiServerImpl" %}
* **MBeanServer mbeanServer**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServer mbeanServer" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [MalformedURLException](/Java/MalformedURLException/), [IOException](/Java/IOException/)

## Clase Padre
[RMIConnectorServer](/Java/RMIConnectorServer/)

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
