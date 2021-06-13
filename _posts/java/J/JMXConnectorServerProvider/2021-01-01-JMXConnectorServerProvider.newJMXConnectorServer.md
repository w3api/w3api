---
title: JMXConnectorServerProvider.newJMXConnectorServer()
permalink: /Java/JMXConnectorServerProvider/newJMXConnectorServer/
date: 2021-01-11
key: Java.J.JMXConnectorServerProvider
category: Java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnectorServerProvider.metodos valor="newJMXConnectorServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JMXConnectorServer newJMXConnectorServer(JMXServiceURL serviceURL, Map<String,?> environment, MBeanServer mbeanServer) throws IOException
~~~

## Parámetros
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}
* **JMXServiceURL serviceURL**,  {% include w3api/param_description.html metodo=_dato parametro="JMXServiceURL serviceURL" %}
* **MBeanServer mbeanServer**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServer mbeanServer" %}

## Excepciones
[IOException](/Java/IOException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JMXConnectorServerProvider](/Java/JMXConnectorServerProvider/)

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
